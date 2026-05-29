# ============================================
# CodSoft Internship - Task 5: Contact Book
# ============================================

import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def display_contact(contact, index=None):
    prefix = f"{index}. " if index else "   "
    print(f"\n{prefix}👤 {contact['name']}")
    print(f"   📞 Phone  : {contact['phone']}")
    print(f"   📧 Email  : {contact['email']}")
    print(f"   🏠 Address: {contact['address']}")
    print("   " + "-" * 35)

def view_all_contacts(contacts):
    if not contacts:
        print("\n📭 Koi contact nahi hai!")
        return
    print(f"\n📒 Contact Book ({len(contacts)} contacts):")
    print("=" * 40)
    for i, c in enumerate(contacts, 1):
        print(f"{i}. 👤 {c['name']}  |  📞 {c['phone']}")
    print("=" * 40)

def add_contact(contacts):
    print("\n➕ New Contact Add Karo:")
    print("-" * 35)
    name    = input("Naam: ").strip()
    phone   = input("Phone number: ").strip()
    email   = input("Email: ").strip()
    address = input("Address: ").strip()

    if not name or not phone:
        print("❌ Naam aur phone number zaroori hai!")
        return

    # Check duplicate phone
    for c in contacts:
        if c["phone"] == phone:
            print(f"⚠️ Yeh number pehle se hai: {c['name']}")
            return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email if email else "N/A",
        "address": address if address else "N/A"
    })
    save_contacts(contacts)
    print(f"✅ Contact add ho gaya: {name}")

def search_contact(contacts):
    if not contacts:
        print("\n📭 Koi contact nahi hai!")
        return

    query = input("\n🔍 Naam ya phone number se search karo: ").strip().lower()
    results = [c for c in contacts
               if query in c["name"].lower() or query in c["phone"]]

    if results:
        print(f"\n🔍 {len(results)} result(s) mile:")
        for c in results:
            display_contact(c)
    else:
        print("❌ Koi contact nahi mila!")

def update_contact(contacts):
    view_all_contacts(contacts)
    if not contacts:
        return

    try:
        num = int(input("\nKaunsa contact update karna hai? (number): "))
        if not (1 <= num <= len(contacts)):
            print("❌ Invalid number!")
            return
    except ValueError:
        print("❌ Sirf number likho!")
        return

    c = contacts[num - 1]
    print(f"\n✏️ Update karo (Enter dabao agar same rakhna hai):")
    print(f"Current naam: {c['name']}")

    new_name    = input(f"Naya naam [{c['name']}]: ").strip()
    new_phone   = input(f"Naya phone [{c['phone']}]: ").strip()
    new_email   = input(f"Naya email [{c['email']}]: ").strip()
    new_address = input(f"Naya address [{c['address']}]: ").strip()

    if new_name:    c["name"]    = new_name
    if new_phone:   c["phone"]   = new_phone
    if new_email:   c["email"]   = new_email
    if new_address: c["address"] = new_address

    save_contacts(contacts)
    print(f"✅ Contact update ho gaya: {c['name']}")

def delete_contact(contacts):
    view_all_contacts(contacts)
    if not contacts:
        return

    try:
        num = int(input("\nKaunsa contact delete karna hai? (number): "))
        if not (1 <= num <= len(contacts)):
            print("❌ Invalid number!")
            return
    except ValueError:
        print("❌ Sirf number likho!")
        return

    c = contacts.pop(num - 1)
    save_contacts(contacts)
    print(f"🗑️ Contact delete ho gaya: {c['name']}")

def main():
    print("=" * 40)
    print("   📒 CodSoft - Contact Book App   ")
    print("=" * 40)

    contacts = load_contacts()

    while True:
        print("\n📌 Menu:")
        print("1. Saare contacts dekho")
        print("2. Contact add karo")
        print("3. Contact search karo")
        print("4. Contact update karo")
        print("5. Contact delete karo")
        print("6. Exit")

        choice = input("\nOption choose karo (1-6): ").strip()

        if choice == "1":
            view_all_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("👋 Contact Book band ho gaya!")
            break
        else:
            print("❌ Invalid! 1-6 ke beech choose karo.")

if __name__ == "__main__":
    main()
