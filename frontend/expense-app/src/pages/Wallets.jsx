import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";

import { GetWallets } from "../api/Wallets-api";
import { useNavigate } from "react-router-dom";


export default function Wallets(){
    const [data, setData] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        async function fetchWallets() {
            const result = await GetWallets();
            setData(result)
        }

        fetchWallets();
    }, []);

    return(
        <>
            <button onClick={() => navigate("/add_wallet")} >+ Add</button>
            <table>
                <tbody>
                    <tr>
                        <th>S.No</th>
                        <th>Name</th>
                        <th>Balance</th>
                    </tr>
                    {data.map((wallet, index) => (
                        <tr key={wallet.id}>
                            <td>{index+1}</td>
                            <td>{wallet.name}</td>
                            <td>{wallet.balance}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </>
    )
}