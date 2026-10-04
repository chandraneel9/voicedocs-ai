import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    Accept: "application/json",
  },
});

export async function healthCheck() {
  const response = await api.get("/api/health");

  return response.data;
}

export async function askQuestion(question) {
  const response = await api.post("/api/chat", {
    question,
  });

  return response.data;
}

export async function uploadDocument(file) {
  const formData = new FormData();

  formData.append("file", file);

  const response = await api.post(
    "/api/documents/upload",
    formData
  );

  return response.data;
}

export async function uploadAudio(file) {
  const formData = new FormData();

  formData.append("file", file);

  const response = await api.post(
    "/api/audio/process",
    formData
  );

  return response.data;
}

export default api;