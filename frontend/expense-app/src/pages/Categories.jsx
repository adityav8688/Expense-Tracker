import { useEffect, useState } from "react";

import { GetCategories } from "../api/Categories-api";

export default function Categories() {
    const [data, setData] = useState([]);

    useEffect(() => {
        async function  fetchCategories() {
            const result = await GetCategories();
            setData(result)
        }

        fetchCategories();
    }, []);

    return(
        <>
            <table>
                <tbody>
                    <tr>
                        <th>S.no</th>
                        <th>Name</th>
                        <th>Type</th>
                    </tr>
                    {data.map((category, index) =>(
                        <tr key={category.id}>
                            <td>{index+1}</td>
                            <td>{category.name}</td>
                            <td>{category.type}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </>
    )
}