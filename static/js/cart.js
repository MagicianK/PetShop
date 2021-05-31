var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', function(){
      var productId = this.dataset.products
      var action = this.dataset.action
      console.log('productId: ', productId, 'Action: ', action)
  })
}
