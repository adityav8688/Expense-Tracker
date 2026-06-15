import { api } from "./login-api";

function errorLog(error){
    console.log("Error", error);
    console.log("Status Code", error.response?.status);
    console.log("Details", error.response?.data);
}

export async function GetTransactions(){
    try{
        const response = await api.get(
            "/transaction"
        )
        return response.data
    } catch (error) {
        errorLog(error);
        throw error;
    }
}

export async function PostTransaction(data) {
    try{
        const response = await api.post(
            "/transaction",
            data,
        );

        return response.data
    } catch (error){
        errorLog(error);
        throw error.response;
    }
}