import { api } from "./login-api";

export async function GetWallets(){
    try{
        const response = await api.get(
            "/wallet"
        );
        return response.data
    } catch (error) {
        console.log("Error :", error);
        console.log("Status: ", error.response?.status);
        console.log("details :", error.response?.data);
    }
}