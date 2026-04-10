import { StreamVideoClient } from "@stream-io/video-react-sdk";
import { useEffect, useRef, useState } from "react";
import { StreamChat } from "stream-chat";

export function useStreamClients({ apiKey, user, token }) {
  const [videoClient, setVideoClient] = useState(null);
  const [chatClient, setChatClient] = useState(null);

  const connectedRef = useRef(false);

  useEffect(() => {
    if (!user || !token || !apiKey || connectedRef.current) return;

    let myVideoClient;
    let myChatClient;

    const initClients = async () => {
      try {
        const tokenProvider = () => Promise.resolve(token);

        // ✅ VIDEO CLIENT
        myVideoClient = StreamVideoClient.getOrCreateInstance({
          apiKey,
          user,
          tokenProvider,
        });

        // 🔥 IMPORTANT FIX
        await myVideoClient.connectUser(user, token);

        // ✅ CHAT CLIENT
        myChatClient = StreamChat.getInstance(apiKey);

        if (!myChatClient.userID) {
          await myChatClient.connectUser(user, token);
        }

        connectedRef.current = true;

        setVideoClient(myVideoClient);
        setChatClient(myChatClient);

      } catch (e) {
        console.error("Error initializing clients:", e);
      }
    };

    initClients();

    return () => {
      if (myVideoClient) {
        myVideoClient.disconnectUser().catch(() => {});
      }
      if (myChatClient) {
        myChatClient.disconnectUser().catch(() => {});
      }
      connectedRef.current = false;
    };
  }, [apiKey, user, token]);

  return { videoClient, chatClient };
}