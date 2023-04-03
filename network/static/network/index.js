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

  document.querySelector('body').onload = loadPosts('all', username);
    document.querySelector('#new_post').onsubmit = newPost;
});


function newPost(event){
    event.preventDefault();
    const content = document.querySelector('#content').value;

    fetch('/posts', {
        method: 'POST',
        body: JSON.stringify({
            content: content
        })
      })
      
      .then(response => response.json())
      .then(result => {
        document.querySelector('#content').value = '';
        console.log(result.message);
        loadPosts('all', username);
      });
}
