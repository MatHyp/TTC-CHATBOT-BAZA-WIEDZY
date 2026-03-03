import axios from "axios";

export async function AI(prompt) {
  try {
    const response = await axios.post(
      `https://${process.env.REACT_APP_BASE_URL}/v1/generate`,
      {
        prompt: prompt
      },
      {
        headers: {
          "Content-Type": "application/json",
          "X-API-Key": process.env.REACT_APP_API_KEY
        }
      }
    );

    return response.data;

  } catch (error) {
    console.error("Błąd:", error.message);
    throw error;
  }
}