import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'

import Login from './pages/login'
import Transactions from './pages/transactions'
import './App.css'

export default function App() {
  return (
    <Routes>
      <Route path='/' element={<Login />} />
      <Route path='/transactions' element={<Transactions />} />
    </Routes>
  )
}

