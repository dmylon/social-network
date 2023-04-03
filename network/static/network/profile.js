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
    window.onload = loadPosts(id,username);
    
    if(document.getElementById('follow-button') != null){
      
      document.querySelector('#follow-button').addEventListener('click', () => {
      
        let follow = false;
        if(document.querySelector('#follow-button').innerHTML == "Follow"){
          follow = true;
        }
        else{
          follow = false;
        }
  
        fetch('/follow', {
          method: 'PUT',
          body: JSON.stringify({
              username: userf,
              follow:follow
          })
        })
    
        if(follow){
          document.querySelector('#follow-button').innerHTML = "Unfollow";
          document.querySelector('#followers').innerHTML++;
        }
        else{
          document.querySelector('#follow-button').innerHTML = "Follow";
          document.querySelector('#followers').innerHTML--;
        }
        
      });
    }
})
