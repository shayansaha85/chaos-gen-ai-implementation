function sendMessage() {
    var messageInput = document.getElementById('message-input');
    var message = messageInput.value;
  
    if (message.trim() !== '') {
      var chatBox = document.getElementById('chat-box');
      var newMessage = document.createElement('div');
      newMessage.textContent = message;
      chatBox.appendChild(newMessage);
  
      // Clear input after sending message
      messageInput.value = '';
    }
  }
  