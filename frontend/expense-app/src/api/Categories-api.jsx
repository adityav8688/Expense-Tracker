import { api } from "./login-api";

function errorLog(error){
    console.log("Error: ", error);
    console.log("Status: ", error.response?.status);
    console.log("Details: ", error.response?.data);
}

export async function GetCategories() {
    try{
        const response = await api.get(
            "/category"
        );
        return response.data
    } catch (error){
        errorLog(error);
    }
}

export async function PostCategory(data) {
    try{
        const response = await api.post(
            "/category",
            data
        )
        return response
    }catch(error){
        errorLog(error);
        throw(error)
    }
}

export async function DelCategory(id, force) {
    try{
        const response = await api.delete(
            `/category/${id}`,
            {
                params: {force},
            }
        )

        return response.data;
    }catch (error){
        if(error.response?.status === 409 && error.response?.data?.detail?.message){
            alert("409 it is");
        }
        errorLog(error)
        throw(error.response?.data)
    }
}

