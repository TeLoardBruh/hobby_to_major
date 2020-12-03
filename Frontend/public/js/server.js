db.collection('students').get().then((doc)=>{
    doc.docs.forEach(element => {
        console.log(element.data());
    });
    
})