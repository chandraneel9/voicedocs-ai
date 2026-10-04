import { useRef, useState } from "react";
import {
  Upload,
  FileText,
  Music,
  Video,
  X,
} from "lucide-react";

function UploadPanel({
  onClose,
  onUpload,
}) {
  const inputRef = useRef(null);

  const [isDragging, setIsDragging] = useState(false);

  function handleFiles(files) {
    if (!files || files.length === 0) {
      return;
    }

    Array.from(files).forEach((file) => {
      onUpload(file);
    });

    onClose();
  }

  function handleDrop(event) {
    event.preventDefault();

    setIsDragging(false);

    handleFiles(event.dataTransfer.files);
  }

  function getFileIcon(file) {
    if (file.type.startsWith("audio/")) {
      return <Music size={28} />;
    }

    if (file.type.startsWith("video/")) {
      return <Video size={28} />;
    }

    return <FileText size={28} />;
  }

  return (
    <div className="modal-backdrop">
      <div className="upload-modal">
        <div className="upload-modal-header">
          <div>
            <h3>Upload to VoiceDocs</h3>
            <p>
              Add documents, audio recordings or videos.
            </p>
          </div>

          <button
            className="close-button"
            onClick={onClose}
          >
            <X size={19} />
          </button>
        </div>

        <div
          className={`drop-zone ${
            isDragging ? "dragging" : ""
          }`}
          onDragOver={(event) => {
            event.preventDefault();
            setIsDragging(true);
          }}
          onDragLeave={() => setIsDragging(false)}
          onDrop={handleDrop}
          onClick={() => inputRef.current?.click()}
        >
          <div className="drop-icon">
            <Upload size={30} />
          </div>

          <h4>
            Drop files here or click to browse
          </h4>

          <p>
            PDF, TXT, MP3, WAV, MP4 and other supported
            formats
          </p>

          <input
            ref={inputRef}
            type="file"
            hidden
            multiple
            accept=".pdf,.txt,.mp3,.wav,.m4a,.mp4,.mov"
            onChange={(event) =>
              handleFiles(event.target.files)
            }
          />
        </div>

        <div className="upload-info">
          <div>
            <FileText size={17} />
            Documents
          </div>

          <div>
            <Music size={17} />
            Audio
          </div>

          <div>
            <Video size={17} />
            Video
          </div>
        </div>
      </div>
    </div>
  );
}

export default UploadPanel;