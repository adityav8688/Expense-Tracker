import { data } from "react-router-dom";
import { api } from "./login-api";

function errorLog(error){
    console.log("Error :", error);
    console.log("Status: ", error.response?.status);
    console.log("details :", error.response?.data);
}

export async function GetWallets(){
    try{
        const response = await api.get(
            "/wallet"
        );
        return response.data
    } catch (error) {
        errorLog(error);
    }
}

export async function  SetWallet(data) {
    try{
        const response = await api.post(
            "/wallet",
            data
        )
    } catch (error) {
        errorLog(error);
        throw (error);
    }
}

export async function DeleteWallet(id, force) {
    try{
        const response = await api.delete(
            `/wallet/${id}`,
            {
                params: {force},
            }
        );
    }catch(error){
        errorLog(error);
        return (error?.response);
    }
}