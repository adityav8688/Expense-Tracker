import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'

import Login from './pages/login'
import Transactions from './pages/transactions'
import Layout from './components/Layout'
import Categories from './pages/Categories'
import Wallets from './pages/Wallets'
import AddWallet from './pages/add_wallet'
import Register from './pages/Register'
import './App.css'

export default function App() {
  return (
    <>
      
    <Routes>
      <Route path='/' element={<Login />} />
      <Route path='/register' element={<Register />} />
      <Route element={<Layout />}>
        <Route path='/transactions' element={<Transactions />} />
        <Route path='/categories' element={<Categories />} />
        <Route path='/wallets' element={<Wallets/>} />
        <Route path='/add_wallet' element={<AddWallet />} />
      </Route>
    </Routes>
    </>
  )
}

