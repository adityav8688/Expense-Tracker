import { useEffect, useState } from "react";

import { GetTransactions } from "../api/login-api";

export default function Transactions(){
    const [data, setData] = useState([])

    useEffect(() => {        
        async function fetchTransactions() {
            const result = await GetTransactions();
            setData(result);
        }

        fetchTransactions();
    }, []);
    return (
        <pre>{JSON.stringify(data, null, 2)}</pre>
    )
}