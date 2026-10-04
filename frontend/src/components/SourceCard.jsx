import {
  FileText,
  Mic,
  Video,
  ExternalLink,
} from "lucide-react";

function SourceCard({ source }) {
  const Icon =
    source.source_type === "audio"
      ? Mic
      : source.source_type === "video"
      ? Video
      : FileText;

  let location = "";

  if (source.source_type === "audio") {
    location = `${formatTime(source.start)} - ${formatTime(
      source.end
    )}`;
  } else if (source.source_type === "video") {
    location = `${formatTime(source.start)} - ${formatTime(
      source.end
    )}`;
  } else if (source.page) {
    location = `Page ${source.page}`;
  }

  return (
    <div className="source-card">
      <div className="source-icon">
        <Icon size={17} />
      </div>

      <div className="source-content">
        <strong>{source.filename}</strong>

        <span>
          {source.source_type?.toUpperCase() || "DOCUMENT"}
          {location ? ` • ${location}` : ""}
        </span>
      </div>

      <button className="source-open">
        <ExternalLink size={15} />
      </button>
    </div>
  );
}

function formatTime(seconds) {
  if (seconds === undefined || seconds === null) {
    return "00:00";
  }

  const totalSeconds = Math.floor(Number(seconds));

  const minutes = Math.floor(totalSeconds / 60);
  const remainingSeconds = totalSeconds % 60;

  return `${String(minutes).padStart(2, "0")}:${String(
    remainingSeconds
  ).padStart(2, "0")}`;
}

export default SourceCard;