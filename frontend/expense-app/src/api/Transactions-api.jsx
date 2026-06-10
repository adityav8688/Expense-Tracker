import { api } from "./login-api";

export async function GetTransactions(){
    try{
        const response = await api.get(
            "/transaction"
        )
        return response.data
    } catch (error) {
        throw error;
        console.log("Error", error);
        console.log("Status Code", error.response?.status);
        console.log("Details", error.response?.data)
    }
}