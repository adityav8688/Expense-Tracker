import { useState } from "react";
import { api } from "../api/login-api";
import { PostCategory } from "../api/Categories-api";

export default function AddCategory(){
    const [name, setName] = useState("");
    const [type, setType] = useState("");
    const [okay, setOkay] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        e.stopPropagation();

        const result = await PostCategory({"name": name,"type": type});
        if(result.status === 200){
            setOkay("Category Created");
            alert("category added");
        }else{
            alert("some error");
        }
    }

    return (
        <>
            <div>
                <form onSubmit={handleSubmit}>
                    <label >Name:
                    <input
                    placeholder="Category Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    />
                    </label>
                    <label >Amount:
                    <select value={type} onChange={(e) => setType(e.target.value)}>
                        <option value="" disabled>no option</option>
                        <option value="income">Income</option>
                        <option value="expense">Expense</option>
                    </select>
                    {okay && <div style={{backgroundColor:"green"}}>{okay}</div>}
                    <button>Add Category</button>
                    </label>
                </form>
            </div>
        </>
    )
}