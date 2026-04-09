import { StreamChat } from "stream-chat";

const apiKey = process.env.NEXT_PUBLIC_STREAM_API_KEY;
const apiSecret = process.env.STREAM_API_SECRET;

export async function POST(request) {
  try {
    const { userId } = await request.json();

    if (!apiKey || !apiSecret) {
      return Response.json(
        { error: "Missing API credentials" },
        { status: 500 }
      );
    }

    // ✅ Correct way to create server client
    const serverClient = StreamChat.getInstance(apiKey, apiSecret);

    const newUser = {
      id: userId,
      name: userId,
    };

    // ✅ Correct method
    await serverClient.upsertUser(newUser);

    // ✅ Correct token method
    const token = serverClient.createToken(userId);

    return Response.json({ token });

  } catch (error) {
    console.error("Error generating user token:", error);
    return Response.json(
      { error: "Failed to generate user token" },
      { status: 500 }
    );
  }
}