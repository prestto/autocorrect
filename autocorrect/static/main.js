var tweetBody = document.querySelector('.tweet-body')
var nextTweet = document.querySelector('#next-button')

var loadTweet = function () {
  // kill old tweet
  tweetBody.innerHTML = ''

  // get request to random tweet url
  var url = 'serve-random'
  var xmlHttp = new XMLHttpRequest()
  xmlHttp.onreadystatechange = function () {
    if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
      tweetBody.innerHTML = xmlHttp.responseText
    }
  }
  xmlHttp.open('GET', url, true)
  xmlHttp.send(null)
}

nextTweet.addEventListener('click', loadTweet)
