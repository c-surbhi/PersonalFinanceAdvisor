import { useState } from 'react'
import ReactMarkdown from 'react-markdown'
import './App.css'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')

  const sendMessage = async () => {
    if (!input.trim()) return
    const userMessage = { text: input, sender: 'user' }
    setMessages([...messages, userMessage])
    setInput('')

    try {
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_input: input })
      })
      const data = await response.json()
      const botMessage = { text: data.response, sender: 'bot' }
      setMessages(prev => [...prev, botMessage])
    } catch (error) {
      const errorMessage = { text: 'Error: Could not connect to backend', sender: 'bot' }
      setMessages(prev => [...prev, errorMessage])
    }
  }

  return (
    <div className="App">
      <h1>Personal Finance Advisor</h1>
      <div className="chat-container">
        <div className="messages">
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.sender}`}>
              <strong>{msg.sender === 'user' ? 'You' : 'Advisor'}:</strong>
              {msg.sender === 'bot' ? (
                <div className="markdown-content">
                  <ReactMarkdown>{msg.text}</ReactMarkdown>
                </div>
              ) : (
                <span>{msg.text}</span>
              )}
            </div>
          ))}
        </div>
        <div className="input-container">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Ask about your spending..."
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
    </div>
  )
}

export default App