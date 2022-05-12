console.log('its adwoaaaa')


const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-tracker')
    const info = modalBtn.getAttribute('data-info')
    

    modalBody.innerHTML = `
        <div class="h5 mb-3">Details on "<b>${name}</b>" .</div>
        <div class="text-muted">
            <p>
                <b>${info}</b>
            </p>
        </div>
    `
    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
    
}))