import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'

import Login from './pages/login'
import Transactions from './pages/transactions'
import Layout from './components/Layout'
import Categories from './pages/Categories'
import Wallets from './pages/Wallets'
import './App.css'

export default function App() {
  return (
    <>
      
    <Routes>
      <Route path='/' element={<Login />} />
      <Route element={<Layout />}>
        <Route path='/transactions' element={<Transactions />} />
        <Route path='/categories' element={<Categories />} />
        <Route path='/wallets' element={<Wallets/>} />
      </Route>
    </Routes>
    </>
  )
}

