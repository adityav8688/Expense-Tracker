import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { GetTransactions } from "../api/Transactions-api";

export default function Transactions(){
    const [data, setData] = useState([])

    const navigate = useNavigate();

    useEffect(() => {        
        async function fetchTransactions() {
            const result = await GetTransactions();
            setData(result);
            
        }

        fetchTransactions();
    }, []);
    return (
        <>
            <button onClick={() => navigate("/add_transaction")}>+ Add</button>
            <table>
                <tbody>
                    <tr>
                        <th>S.NO</th>
                        <th>Category</th>
                        <th>Type</th>
                        <th>Title</th>
                        <th>Amount</th>
                        <th>Date</th>
                    </tr>
                    {data.map((transaction, index) => (
                        <tr key={transaction.id}>
                            <td>{index+1}</td>
                            <td>{transaction.category_id}</td>
                            <td>{transaction.type}</td>
                            <td>{transaction.title}</td>
                            <td>{transaction.amount}</td>
                            <td>{new Date(transaction.transaction_date).toLocaleDateString('en-GB')}</td>
                            <td>
                                <button
                                style={{backgroundColor:"red"}}
                                >
                                Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </>
    );
}