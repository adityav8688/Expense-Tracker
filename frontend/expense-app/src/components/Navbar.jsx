import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

export default function Navbar() {
    const navigate = useNavigate();

    function handleClick(){
        localStorage.removeItem("token");
        navigate("/");
    }

    return (
        <nav>
            <Link to="/">Home</Link>
            {" | "}
            <Link to="/transactions">Transactions</Link>
            {" | "}
            <Link to="/categories">Categories</Link>
            {" | "}
            <Link to="/wallets">Wallets</Link>
            {" | "}
            <button onClick={()=> handleClick()}>logout</button>
        </nav>
    )
}