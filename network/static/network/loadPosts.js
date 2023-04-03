function likePost(post,type,username,unlike){

    fetch(('/post/' + post.id) , {
        method: 'PUT',
        body: JSON.stringify({
            username: username,
            unlike : unlike
        })
      })

      loadPosts(type,username);
      loadPosts(type,username);
}


function requestEdit(post,new_content){
    
    fetch(('/post/' + post.id) , {
        method: 'PUT',
        body: JSON.stringify({
            content: new_content
        })
      })
    
}


function editPost(post,type,username){

    const container = document.querySelector('#container-' + post.id);
    const textbox = document.createElement('textarea');
    textbox.innerHTML = post.content;
    textbox.className = 'form-control';
    textbox.id = 'text-' + post.id;
    const saveBtn = document.createElement('button');
    saveBtn.id = 'save-' + post.id;
    saveBtn.className = 'btn btn-primary';
    saveBtn.innerHTML = 'Save Changes';
    saveBtn.style.display = 'block';
    saveBtn.addEventListener('click', () => {
        requestEdit(post, textbox.value);
        textbox.style.display = 'none';
        saveBtn.style.display = 'none';
        document.querySelector('#edit-' + post.id).style.display = 'block';
        document.querySelector('#timestamp-' + post.id).style.display = 'block';
        document.querySelector('#content-' + post.id).style.display = 'block';
        loadPosts(type,username);
        loadPosts(type,username);
    });

    document.querySelector('#edit-' + post.id).style.display = 'none';
    document.querySelector('#timestamp-' + post.id).style.display = 'none';
    document.querySelector('#content-' + post.id).style.display = 'none';
    container.insertBefore(textbox, container.childNodes[1]);
    container.insertBefore(saveBtn, container.childNodes[2]);
}



function loadPosts(type,username){

    fetch('/posts/'+ type + '?page='+document.querySelector('#page').value) 
    .then(response => response.json())
    .then(posts => {
           
        console.log(posts);

        document.querySelector("#post-view").innerHTML = '';
        document.querySelector('#next').disabled = true;


        posts.forEach(post => {
            const container = document.createElement('div');
            container.className = "post-container";
            container.id = 'container-' + post.id;
            container.style.paddingLeft = '2vw';
            container.style.paddingTop = '2vw';
            container.style.paddingBottom = '2vw';
            container.style.paddingRight = '2vw';
            const author = document.createElement('h2');
            author.style.marginBottom = '4vh';
            const author_link = document.createElement('a');
            author_link.href = '/pages/' + post.owner;
            author_link.innerHTML = post.owner;
            author_link.style.color = 'black';
            const content = document.createElement('p');
            content.style.marginBottom = '4vh';
            content.id = 'content-' + post.id;
            content.innerHTML = post.content;
            

            const timestamp = document.createElement('p');
            timestamp.innerHTML = post.date
            timestamp.style.color = 'gray';
            timestamp.id = 'timestamp-' + post.id;
            const likeButton = document.createElement('button');
            likeButton.className = 'like-button';
            likeButton.id = 'like-'+post.id;
            const btnImg = document.createElement('img');
            btnImg.className = 'like-icon';
            btnImg.id = 'like-img' + post.id;

            if (post.liked == false){
                btnImg.src = whiteImgPath;
            }
            else{
                btnImg.src = redImgPath;
            }

            btnImg.addEventListener('click', () => {
                if(btnImg.src.includes('red')){
                    unlike = true;
                }
                else{
                    unlike = false;
                }
                likePost(post,type,username,unlike);
            });

            
            if(post.next == document.querySelector('#page').value){
                document.querySelector('#next').disabled = true;
            }
            else{
                document.querySelector('#next').disabled = false;
            }
            const likes = document.createElement('strong');
            likes.innerHTML = post.likes;
            likes.style.marginLeft = '5px';

            document.querySelector('#post-view').append(container);
            container.append(author);
            author.append(author_link);

            if(username == post.owner){
                const edit = document.createElement('a');
                edit.innerHTML = 'Edit';
                edit.id = 'edit-'+ post.id;
                edit.href = 'javascript:void(0)';
                edit.addEventListener('click', () => editPost(post,type,username)); 
                container.append(edit);
            }
            container.append(content);
            container.append(timestamp);
            container.append(likeButton);
            container.append(btnImg);
            container.append(likes);

            
        });
    });

}