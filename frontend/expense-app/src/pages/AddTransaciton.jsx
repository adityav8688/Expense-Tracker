import { use, useEffect, useState } from "react";
import { api } from "../api/login-api";
import { GetCategories } from "../api/Categories-api";
import { GetWallets } from "../api/Wallets-api";
import { PostTransaction } from "../api/Transactions-api";

export default function AddTransaction(){
    const [walletId , setWalletId] = useState("");
    const [categoryId, setCategoryId] = useState("");
    const [type, setType] = useState("");
    const [title, setTitle] = useState("");
    const [date, setDate] = useState("");
    const [amount, setAmount] = useState("");
    const [balance, setBalance] = useState("");
    const [cateogories, setCategories] = useState([]);
    const [wallets, setWallets] = useState([]);

    useEffect(() =>{
        async function fetchCategories() {  
            const result = await GetCategories();
            setCategories(result);
        }
        async function fetchWallets() {
            const result = await GetWallets();
            setWallets(result);
        }

        fetchCategories();
        fetchWallets();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try{
            const payload = {
                walletId: Number(walletId),
                categoryId: Number(categoryId),
                type: type,
                title: title,
                description: "",
                amount: Number(amount),
                transaction_date: date,
            };
            console.log(payload);
            const result = await PostTransaction(payload);
            
            setWalletId("");
            setCategoryId("");
            setType("");
            setTitle("");
            setDate("");
            setAmount("");
        }catch(error){
            alert("something gone wrong")
            alert(error?.data);
            throw error;
        }
    }

    return(
        <>
            <div>Select wallet:
                <select value={walletId} onChange={(e)=> {
                    const wallId = Number(e.target.value);
                    setWalletId(wallId);

                    const selectWallet = wallets.find(
                        w => w.id === wallId
                    );

                    if (selectWallet){
                        setBalance(selectWallet.balance);
                    }
                }}>
                    <option value="" disabled>Select Wallet</option>
                    {wallets.map(wallet => (
                        <option key={wallet.id} value={wallet.id}>
                            {wallet.name}
                        </option>
                    ))}
                </select>
                <h3>Wallet Balance: {balance}</h3>
            </div>
            <form onSubmit={handleSubmit}>
                <label>Category
                    <select value={categoryId} onChange={(e) => {
                        const selectedId = Number(e.target.value);
                        setCategoryId(selectedId);

                        const selectedCategory = cateogories.find(
                            c => c.id === selectedId
                        );

                        if (selectedCategory){
                            setType(selectedCategory.type);
                        }

                    }}>
                        <option value="" disabled>Select Category</option>
                        {cateogories.map(category => (
                            <option key={category.id} value={category.id}>
                                {category.name}
                            </option>
                        ))} 
                    </select>
                </label>
                <label>Type
                    <select disabled value={type} onChange={(e)=>setType(e.target.value)}>
                        <option value="" disabled>Select Type</option>
                        <option value="income">Income</option>
                        <option value="expense">Expense</option>
                    </select>
                </label>
                <label>Title
                    <input 
                    type="text"
                    placeholder="enter title"
                    value={title}
                    onChange={(e)=>setTitle(e.target.value)}
                    ></input>
                </label>
                <label>Amount
                    <input
                    type="number"
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                    placeholder="enter amount"
                    ></input>
                </label>
                <label>Date
                    <input 
                    type="date"
                    value={date}
                    onChange={(e)=>setDate(e.target.value)}
                    ></input>
                </label>
                <button type="submit">Save</button>
            </form>
        </>
    )
}