import { useState } from "react";
import Message from "./Message";
import { sendMessage } from "../services/api";

function Chat() {
  const [messages, setMessages] = useState([
    {
      sender: "ai",
      text: "Hi 👋 I'm your Magicpin Merchant Assistant.",
    },
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    const current = input;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: current,
      },
    ]);

    setInput("");
    setLoading(true);

    try {
      const response = await sendMessage(current);

      console.log("Received Response:", response);

      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text:
            response.reply ||
            "Sorry, Magicpin AI is temporarily unavailable.",
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text:
            "Sorry, Magicpin AI is temporarily unavailable.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <h1>Magicpin AI Merchant Assistant</h1>

      <div className="messages">
        {messages.map((msg, index) => (
          <Message
            key={index}
            sender={msg.sender}
            text={msg.text}
          />
        ))}

        {loading && (
          <div className="typing">
            Magicpin AI is typing...
          </div>
        )}
      </div>

      <div className="input-box">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask something..."
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleSend();
            }
          }}
        />

        <button onClick={handleSend}>
          Send
        </button>
      </div>
    </div>
  );
}

export default Chat;