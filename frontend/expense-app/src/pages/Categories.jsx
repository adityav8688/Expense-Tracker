import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { GetCategories, DelCategory } from "../api/Categories-api";

export default function Categories() {
    const [data, setData] = useState([]);
    const [force, setForce] = useState(false);
    const navigate = useNavigate();

    const handleDelete = async (category) => {

        const result = await DelCategory(category.id, force);
        const msg = result.detail?.message || result.detail;

        const updateData = await GetCategories();
        setData(updateData);
}

    const handleAdd = async () => {
        const result = await AddCategory();
    }

    useEffect(() => {
        async function  fetchCategories() {
            const result = await GetCategories();
            setData(result)
        }

        fetchCategories();
    }, []);

    return(
        <>
            <button onClick={()=> navigate("/add_category")}>+ Add</button>
            <table>
                <tbody>
                    <tr>
                        <th>S.no</th>
                        <th>Name</th>
                        <th>Type</th>
                    </tr>
                    {data.map((category, index) =>(
                        <tr key={category.id} id={category.id}>
                            <td>{index+1}</td>
                            <td>{category.name}</td>
                            <td>{category.type}</td>
                            <td>
                                <button 
                                style={{backgroundColor:"red", borderRadius: "2.5px"}}
                                onClick={() => handleDelete(category)}
                                >
                                Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

        </>
    )
}