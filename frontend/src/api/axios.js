import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // FastAPI default
  withCredentials: true,           // enable cookies if using JWT cookies
});

export default api;