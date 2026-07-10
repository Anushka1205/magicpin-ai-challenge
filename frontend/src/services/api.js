import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const createContext = async () => {
  try {
    const response = await API.post("/v1/context", {
      scope: "merchant",
      context_id: "merchant_001",
      version: 1,
      payload: {
        name: "ABC Restaurant",
        city: "Delhi",
        category: "Restaurant",
      },
    });

    console.log("Context Created:", response.data);
    return response.data;
  } catch (error) {
    console.error("Context Error:", error);
  }
};

export const sendMessage = async (message) => {
  try {
    const response = await API.post("/v1/message", {
      conversation_id: "demo_conversation",
      message: message,
    });

    console.log("Backend Response:", response.data);

    return response.data;
  } catch (error) {
    console.error("API Error:", error);

    if (error.response) {
      console.error("Response:", error.response.data);
    }

    throw error;
  }
};