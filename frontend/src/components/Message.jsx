function Message({ sender, text }) {
  return (
    <div className={sender === "user" ? "user-message" : "ai-message"}>
      <strong>{sender === "user" ? "You" : "Magicpin AI"}</strong>

      <p>{text}</p>
    </div>
  );
}

export default Message;