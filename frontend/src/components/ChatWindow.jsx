import { useState } from "react";
import {
  Send,
  Mic,
  Sparkles,
} from "lucide-react";

import ChatMessage from "./ChatMessage";
import Loading from "./Loading";

function ChatWindow({
  messages,
  onSendMessage,
  isLoading,
}) {
  const [question, setQuestion] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    const trimmedQuestion = question.trim();

    if (!trimmedQuestion || isLoading) {
      return;
    }

    onSendMessage(trimmedQuestion);

    setQuestion("");
  }

  return (
    <main className="chat-area">
      <div className="chat-header">
        <div>
          <div className="online-status">
            <span></span>
            AI Assistant
          </div>

          <h2>Ask your knowledge base</h2>

          <p>
            Ask questions about your uploaded documents,
            audio and video.
          </p>
        </div>

        <div className="header-ai-icon">
          <Sparkles size={22} />
        </div>
      </div>

      <div className="messages-container">
        {messages.length === 0 ? (
          <div className="welcome-state">
            <div className="welcome-icon">
              <Sparkles size={30} />
            </div>

            <h2>Welcome to VoiceDocs AI</h2>

            <p>
              Upload your files and ask questions about
              their contents.
            </p>

            <div className="suggestion-list">
              <button
                onClick={() =>
                  onSendMessage(
                    "What is this document about?"
                  )
                }
              >
                What is this document about?
              </button>

              <button
                onClick={() =>
                  onSendMessage(
                    "Summarize the uploaded content."
                  )
                }
              >
                Summarize the uploaded content.
              </button>

              <button
                onClick={() =>
                  onSendMessage(
                    "What are the important points?"
                  )
                }
              >
                What are the important points?
              </button>
            </div>
          </div>
        ) : (
          <>
            {messages.map((message, index) => (
              <ChatMessage
                key={index}
                message={message}
              />
            ))}

            {isLoading && <Loading />}
          </>
        )}
      </div>

      <div className="composer-wrapper">
        <form
          className="message-composer"
          onSubmit={handleSubmit}
        >
          <button
            type="button"
            className="composer-icon-button"
            title="Voice input"
          >
            <Mic size={19} />
          </button>

          <input
            type="text"
            placeholder="Ask something about your files..."
            value={question}
            onChange={(event) =>
              setQuestion(event.target.value)
            }
            disabled={isLoading}
          />

          <button
            type="submit"
            className="send-button"
            disabled={!question.trim() || isLoading}
          >
            <Send size={18} />
          </button>
        </form>

        <div className="composer-hint">
          VoiceDocs AI answers using your uploaded content.
        </div>
      </div>
    </main>
  );
}

export default ChatWindow;