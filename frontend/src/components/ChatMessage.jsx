import { User, Sparkles } from "lucide-react";
import SourceCard from "./SourceCard";

function ChatMessage({ message }) {
  const isUser = message.role === "user";

  return (
    <div className={`chat-message ${isUser ? "user" : "assistant"}`}>
      <div className="message-avatar">
        {isUser ? <User size={17} /> : <Sparkles size={17} />}
      </div>

      <div className="message-body">
        <div className="message-label">
          {isUser ? "You" : "VoiceDocs AI"}
        </div>

        <div className="message-text">
          {message.content}
        </div>

        {!isUser &&
          message.sources &&
          message.sources.length > 0 && (
            <div className="sources-section">
              <div className="sources-title">
                Sources
              </div>

              <div className="sources-list">
                {message.sources.map((source, index) => (
                  <SourceCard
                    key={index}
                    source={source}
                  />
                ))}
              </div>
            </div>
          )}
      </div>
    </div>
  );
}

export default ChatMessage;