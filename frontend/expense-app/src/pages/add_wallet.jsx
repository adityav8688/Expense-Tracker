import { useState } from "react";
import { SetWallet } from "../api/Wallets-api";
import { useNavigate } from "react-router-dom";

export default function AddWallet() {
    const [name, setName] = useState("");
    const [balance, setBalance] = useState("");
    const [currency, setCurrency] = useState("");

    const navigate = useNavigate();

    async function handleSubmit() {
        const data = {"name": name, "balance": parseFloat(balance) , "currency": currency}
        SetWallet(data);
    }

    return(
        <>
            <form onSubmit={() => handleSubmit()}>
                <label>Name:
                    <input 
                    type="text"
                    placeholder="Enter Bank name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    />
                </label>
                <label>Balance:
                    <input
                    type="number"
                    placeholder="Enter balance"
                    value={balance}
                    onChange={(e) => setBalance(e.target.value)}
                    />
                </label>
                <label>Currency:
                    <input
                    type="text"
                    placeholder="currency"
                    value={currency}
                    onChange={(e) => setCurrency(e.target.value)}
                    />
                </label>
                <button>Save</button>
                <button onClick={() => navigate('/wallets')}>Back</button>
            </form>
        </>
    )
}