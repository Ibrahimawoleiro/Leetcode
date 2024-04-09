function numUniqueEmails(emails: string[]): number {
    let store: Set<string> = new Set();
    for(let email of emails){
        let splitted: string[] = email.split('@')
        let removed_plus: string = splitted[0].split('+')[0]

        removed_plus = removed_plus.replace(/\./g,'')
        console.log(removed_plus)
        store.add(removed_plus+'@'+splitted[1])
    }
    console.log(store)
    return store.size
};