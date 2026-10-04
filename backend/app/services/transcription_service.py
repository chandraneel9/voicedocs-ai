from faster_whisper import WhisperModel


def transcribe_audio(file_path: str):
    """
    Transcribe an audio file using Faster-Whisper.
    """

    # Load the small Whisper model.
    # The first run downloads the model once.
    model = WhisperModel(
        "tiny",
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(
        file_path,
        beam_size=5
    )

    results = []

    for segment in segments:

        results.append({
            "text": segment.text.strip(),
            "start": round(segment.start, 2),
            "end": round(segment.end, 2)
        })

    return {
        "language": info.language,
        "language_probability": round(
            info.language_probability,
            4
        ),
        "segments": results
    }