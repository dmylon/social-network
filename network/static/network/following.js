import './loadPosts.js'

document.addEventListener('DOMContentLoaded', () => {
    
  if(document.querySelector('#page').value == 1){
    document.querySelector('#previous').disabled = true;
  } 

    document.querySelector('#next').addEventListener('click', () => {
        document.querySelector('#page').value++;
      });
      
      document.querySelector('#previous').addEventListener('click', () => {
        document.querySelector('#page').value--;
      });
    window.onload = loadPosts('following', username);
})