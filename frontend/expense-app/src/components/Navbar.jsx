import { Link } from "react-router-dom";

export default function Navbar() {
    return (
        <nav>
            <Link to="/">Home</Link>
            {" | "}
            <Link to="/transactions">Transactions</Link>
            {" | "}
            <Link to="/categories">Categories</Link>
            {" | "}
            <Link to="/wallets">Wallets</Link>
        </nav>
    )
}