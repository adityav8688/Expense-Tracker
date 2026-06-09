import { useEffect, useState } from "react";
import { GetWallets } from "../api/Wallets-api";

export default function Wallets(){
    const [data, setData] = useState([]);

    useEffect(() => {
        async function fetchWallets() {
            const result = await GetWallets();
            setData(result)
        }

        fetchWallets();
    }, []);

    return(
        <>
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