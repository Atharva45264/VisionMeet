import asyncio
import os
import logging
from uuid import uuid4
from dotenv import load_dotenv

# Vision Agents imports
from vision_agents.core import agents
from vision_agents.plugins import getstream, gemini
from vision_agents.core.edge.types import User

# ❌ REMOVED unsupported core events

# ✅ ONLY supported events
from vision_agents.core.llm.events import (
    RealtimeUserSpeechTranscriptionEvent,
    LLMResponseChunkEvent
)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Meeting data storage
meeting_data = {
    "transcript": [],
    "is_active": False
}

async def start_agent(call_id: str):
    logger.info("🤖 Starting Meeting Assistant...")
    logger.info(f"📞 Call ID: {call_id}")

    agent = agents.Agent(
        edge=getstream.Edge(),
        agent_user=User(
            id="meeting-assistant-bot",
            name="Meeting Assistant"
        ),
        instructions="""
        You are a meeting transcription bot.

        RULES:
        - Only respond when user says "Hey Assistant"
        - Otherwise stay silent
        - Transcribe everything
        """,
        llm=gemini.Realtime(fps=0),
    )

    meeting_data["agent"] = agent
    meeting_data["call_id"] = call_id

    # ✅ TRANSCRIPTION HANDLER
    @agent.events.subscribe
    async def handle_transcript(event: RealtimeUserSpeechTranscriptionEvent):
        if not event.text or not event.text.strip():
            return

        speaker = getattr(event, "participant_id", "Unknown")
        transcript_text = event.text.strip()

        meeting_data["transcript"].append({
            "speaker": speaker,
            "text": transcript_text,
            "timestamp": getattr(event, "timestamp", None)
        })

        logger.info(f"📝 [{speaker}]: {transcript_text}")

        # Q&A trigger
        if transcript_text.lower().startswith("hey assistant"):
            question = transcript_text[13:].strip()

            if question:
                logger.info(f"❓ Q&A triggered: {question}")

                context = "MEETING TRANSCRIPT:\n\n"
                for entry in meeting_data["transcript"]:
                    context += f"[{entry['speaker']}]: {entry['text']}\n"

                prompt = f"""
                {context}

                USER QUESTION: {question}

                Answer based ONLY on transcript. Keep it short.
                """

                try:
                    await agent.simple_response(prompt)
                    logger.info("🤖 Responding...")
                except Exception as e:
                    logger.error(f"❌ Q&A error: {e}")

    # ✅ LLM RESPONSE HANDLER
    @agent.events.subscribe
    async def handle_llm_response(event: LLMResponseChunkEvent):
        if getattr(event, "delta", None):
            logger.info(f"🤖 {event.delta}")

    # Initialize agent
    call = agent.edge.client.video.call("default", call_id)

    logger.info("✅ Joining call...")

    try:
        async with agent.join(call):  # ✅ FIXED
            logger.info("\n" + "=" * 60)
            logger.info("🎙️ MEETING ASSISTANT ACTIVE!")
            logger.info("=" * 60)
            logger.info("📋 Features:")
            logger.info("   1. Auto-transcription")
            logger.info("   2. Q&A (Hey Assistant)")
            logger.info(f"🔗 Meeting ID: {call_id}")
            logger.info("=" * 60 + "\n")

            await agent.finish()

    except Exception as e:
        logger.error(f"❌ Join error: {e}")

    logger.info("✅ Agent finished")


def print_meeting_summary():
    print("\n" + "=" * 70)
    print("📋 MEETING SUMMARY")
    print("=" * 70)

    for entry in meeting_data["transcript"]:
        print(f"[{entry['speaker']}]: {entry['text']}")

    print("=" * 70 + "\n")


if __name__ == "__main__":
    call_id = os.getenv("CALL_ID", f"meeting-{uuid4().hex[:8]}")

    print("\n🎯 SMART MEETING ASSISTANT\n")

    try:
        asyncio.run(start_agent(call_id))
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user")
    finally:
        if meeting_data["transcript"]:
            print_meeting_summary()