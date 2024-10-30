from flask import Flask, jsonify, request

app = Flask(__name__)
# Flask uygulaması başlatılıyor.

# Öğe listesi: uygulama çalışırken üzerinde işlem yapılacak örnek veriler
items = [
    {"id": 1, "name": "item 1", "description": "this is item 1"},
    {"id": 2, "name": "item 2", "description": "this is item 2"},
]


@app.route("/")
def home():
    # Anasayfa rotası tanımlanıyor. Bu rota, uygulamaya girildiğinde "Welcome to the Home page to do list" yazısını döndürür.
    return "Welcome to the Home page to do list"


@app.route("/items", methods=["GET"])
# "/items" rotasına yapılan GET isteğini işleyen `get_items` adlı fonksiyon tanımlanıyor.
def get_items():
    # Tüm öğeleri JSON formatında döndürür.
    return jsonify(items)

@app.route("/items/<int:item_id>", methods=["GET"])
# Belirli bir item_id'ye göre öğeyi almak için kullanılan fonksiyon
def get_item(item_id):
    # `item_id` parametresini alan bir fonksiyon tanımlanıyor.

    item = next((item for item in items if item["id"] == item_id), None)
    # `items` listesinde `id` değeri `item_id` ile eşleşen ilk öğeyi bulur, eğer yoksa `item` değeri `None` olur.

    if item is None:
        # Eğer `item` bulunamazsa (None ise), hata mesajı içeren bir JSON yanıtı döner.
        return jsonify({"error": "item not found"})

    # `item` bulunduysa, bu öğeyi JSON formatında döndürür.
    return jsonify(item)


@app.route("/items", methods=["POST"])
# "/items" rotasına yapılan POST isteği ile yeni bir öğe oluşturulması için `create_item` fonksiyonu tanımlanıyor.
def create_item():
    # Eğer gelen istek JSON formatında değilse veya "name" anahtarı JSON verisinde yoksa hata döndürür.
    if not request.json or not "name" in request.json:
        return jsonify({"error": "item not found"})
    
    # Yeni öğe sözlüğü oluşturuluyor.
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        # Yeni öğeye, listedeki son öğenin id değerine 1 eklenerek benzersiz bir id atanır. Eğer liste boşsa id 1 olur.
        
        "name": request.json["name"],
        # İstek JSON verisinden gelen "name" değeri alınır ve öğeye eklenir.
        
        "description": request.json["description"]
        # İstek JSON verisinden gelen "description" değeri alınır ve öğeye eklenir.
    }

    items.append(new_item)
    # Yeni oluşturulan öğe `items` listesine eklenir.

    return jsonify(new_item)
    # Yeni öğe JSON formatında yanıt olarak döndürülür.


@app.route("/items/<int:item_id>", methods=["PUT"])
# Belirli bir öğeyi güncellemek için "/items/<int:item_id>" rotasına yapılan `PUT` isteğini işleyen `update_item` fonksiyonu.
def update_item(item_id):
    # `item_id`'ye sahip öğeyi bulmaya çalışır.
    item = next((item for item in items if item["id"] == item_id), None)

    if item is None:
        # Eğer öğe bulunamazsa, hata mesajı içeren bir JSON yanıtı döner.
        return jsonify({"error": "item not found"})
    
    # `name` ve `description` değerleri istekte varsa güncellenir, yoksa mevcut değerler kalır.
    item["name"] = request.json.get("name", item["name"])
    item["description"] = request.json.get("description", item["description"])

    return jsonify(item)
    # Güncellenmiş öğeyi JSON formatında yanıt olarak döner.


@app.route('/items/<int:item_id>', methods=['DELETE'])
# Belirli bir öğeyi silmek için "/items/<int:item_id>" rotasına yapılan DELETE isteğini işleyen `delete_item` fonksiyonu.
def delete_item(item_id):
    global items
    # `items` listesini global olarak tanımlayarak fonksiyon içinde güncelleme yapabiliyoruz.

    items = [item for item in items if item["id"] != item_id]
    # `item_id`'ye sahip olmayan öğelerden oluşan yeni bir liste ile `items` listesini güncelliyoruz.
    # Bu işlem, belirtilen `item_id`'ye sahip öğeyi listeden çıkarmış olur.

    return jsonify({"result": "Item deleted"})
    # İşlem başarılı olduğunda, "Item deleted" mesajını JSON formatında döndürür.


if __name__ == "__main__":
    app.run(debug=True)
    # Uygulamayı başlatır ve hata ayıklama modunu etkinleştirir.
