import { useState } from "react";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import UploadPanel from "../components/UploadPanel";

function Dashboard() {
  const [documents, setDocuments] = useState([
    {
      id: 1,
      name: "CV_2025060511005026.pdf",
      type: "pdf",
    },
    {
      id: 2,
      name: "IoT Mid Term 2 Notes.pdf",
      type: "pdf",
    },
    {
      id: 3,
      name: "voicedocs_test_audio.mp3",
      type: "audio",
    },
  ]);

  const [selectedDocument, setSelectedDocument] =
    useState(null);

  const [showUpload, setShowUpload] =
    useState(false);

  const [isLoading, setIsLoading] =
    useState(false);

  const [messages, setMessages] = useState([]);

  function handleUpload(file) {
    const extension =
      file.name.split(".").pop()?.toLowerCase();

    let type = "pdf";

    if (
      ["mp3", "wav", "m4a"].includes(extension)
    ) {
      type = "audio";
    }

    if (
      ["mp4", "mov", "avi", "mkv"].includes(
        extension
      )
    ) {
      type = "video";
    }

    const newDocument = {
      id: Date.now(),
      name: file.name,
      type,
    };

    setDocuments((previous) => [
      ...previous,
      newDocument,
    ]);
  }

  async function handleSendMessage(question) {
    const userMessage = {
      role: "user",
      content: question,
    };

    setMessages((previous) => [
      ...previous,
      userMessage,
    ]);

    setIsLoading(true);

    /*
     * TEMPORARY FRONTEND DEMO RESPONSE.
     *
     * We will replace this with the FastAPI API
     * after the UI is complete.
     */

    setTimeout(() => {
      const assistantMessage = {
        role: "assistant",
        content:
          "This is a frontend demonstration response. The RAG backend will be connected here next.",
        sources: [
          {
            filename:
              "voicedocs_test_audio.mp3",
            source_type: "audio",
            start: 0,
            end: 6,
          },
          {
            filename:
              "IoT Mid Term 2 Notes.pdf",
            source_type: "pdf",
            page: 1,
          },
        ],
      };

      setMessages((previous) => [
        ...previous,
        assistantMessage,
      ]);

      setIsLoading(false);
    }, 800);
  }

  return (
    <div className="app-shell">
      <Sidebar
        documents={documents}
        selectedDocument={selectedDocument}
        onSelectDocument={setSelectedDocument}
        onUploadClick={() =>
          setShowUpload(true)
        }
      />

      <ChatWindow
        messages={messages}
        onSendMessage={handleSendMessage}
        isLoading={isLoading}
      />

      {showUpload && (
        <UploadPanel
          onClose={() => setShowUpload(false)}
          onUpload={handleUpload}
        />
      )}
    </div>
  );
}

export default Dashboard;