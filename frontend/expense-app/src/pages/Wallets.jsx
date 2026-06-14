import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";

import { GetWallets, DeleteWallet } from "../api/Wallets-api";
import { useNavigate } from "react-router-dom";


export default function Wallets(){
    const [data, setData] = useState([]);
    const [force, setForce] = useState(false)
    const navigate = useNavigate();

    const handleDelete = async (wallet) => {
        
        const result = await DeleteWallet(wallet.id, force);


        if (result?.status === 409){
            const con = confirm(`${result?.data?.detail?.message}`);
            if (con){
                setForce(con);
                DeleteWallet(wallet.id, force);
            }
        }
        
        const updateData = await GetWallets();
        setData(updateData);
    };

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
                            <td>
                                <button 
                                style={{backgroundColor:"red"}} 
                                onClick={() => handleDelete(wallet)}
                                >Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </>
    )
}