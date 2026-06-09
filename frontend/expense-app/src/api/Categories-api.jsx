import { api } from "./login-api";

export async function GetCategories() {
    try{
        const response = await api.get(
            "/category"
        );
        return response.data
    } catch (error){
        console.log("Error: ", error);
        console.log("Status: ", error.response?.status);
        console.log("Details: ", error.response?.data);
    }
}