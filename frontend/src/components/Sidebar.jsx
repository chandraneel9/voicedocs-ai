import {
  FileText,
  Mic,
  Video,
  Upload,
  MessageSquare,
  Search,
} from "lucide-react";

function Sidebar({
  documents,
  selectedDocument,
  onSelectDocument,
  onUploadClick,
}) {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <div className="brand-icon">V</div>

        <div>
          <h1>VoiceDocs</h1>
          <span>AI Intelligence</span>
        </div>
      </div>

      <button className="upload-button" onClick={onUploadClick}>
        <Upload size={18} />
        Upload File
      </button>

      <div className="sidebar-section">
        <div className="sidebar-section-title">
          <span>Library</span>
          <span>{documents.length}</span>
        </div>

        <div className="document-list">
          {documents.length === 0 ? (
            <div className="empty-library">
              <FileText size={22} />
              <p>No files yet</p>
            </div>
          ) : (
            documents.map((document) => {
              const Icon =
                document.type === "audio"
                  ? Mic
                  : document.type === "video"
                  ? Video
                  : FileText;

              return (
                <button
                  key={document.id}
                  className={`document-item ${
                    selectedDocument?.id === document.id
                      ? "active"
                      : ""
                  }`}
                  onClick={() => onSelectDocument(document)}
                >
                  <Icon size={17} />

                  <div className="document-info">
                    <span>{document.name}</span>
                    <small>{document.type}</small>
                  </div>
                </button>
              );
            })
          )}
        </div>
      </div>

      <div className="sidebar-bottom">
        <div className="sidebar-nav-item">
          <Search size={17} />
          Search Library
        </div>

        <div className="sidebar-nav-item">
          <MessageSquare size={17} />
          Conversations
        </div>
      </div>
    </aside>
  );
}

export default Sidebar;