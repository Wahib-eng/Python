

import random
import time

def bubble_sort(arr): #Temel mantık, ardışık elemanları karşılaştıracak, gerektiğinde yer değiştirecek. Her geçişte en büyük eleman, dizinin sonuna yerleşecek.
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Değişkenler arasında değer değişimi yapar bu fonk.
#temp = arr[j]
#arr[j] = arr[j + 1]
#arr[j + 1] = temp gibi.


def insertion_sort(arr):
    for i in range(1, len(arr)): ## İlk eleman zaten sıralı kabul edildiği için 1'den başlarız.
        key = arr[i] # Şu anki elemanı key'e kaydet
        j = i - 1 # Şu anki elemandan bir önceki elemanın indisini belirle
         # key, sıralı kısmın içinde uygun konuma yerleştirilene kadar büyük elemanlarla karşılaştır ve gerektiğinde yer değiştir.
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] # Elemanları kaydır
            j -= 1
        arr[j + 1] = key # key, sıralı kısmın uygun konumuna yerleştirilir

def selection_sort(arr): #Dizinin minimum elemanını seçip, sıralı kısma ekleyecek. Her geçişte en küçük eleman bulacak ve sıralı kısma ekleyecek.
    for i in range(len(arr)):
        min_index = i  # Minimum elemanın indeksini saklamak için bir değişken
        for j in range(i+1, len(arr)): # Dizideki minimum elemanı bulma
            if arr[j] < arr[min_index]:
                min_index = j # Minimum elemanın indeksini güncelleme
        arr[i], arr[min_index] = arr[min_index], arr[i] # En küçük elemanı sıralı kısmın sonuna ekle

def merge_sort(arr): # Diziyi iki eşit parçaya bölecek, her parçayı sıralayacak ve sonra birleştirecek.
    if len(arr) > 1:
        mid = len(arr) // 2 #Diziyi iki eşit parçaya ayırdı
        left_half = arr[:mid] #sol parçası
        right_half = arr[mid:] #sağ parçası

        merge_sort(left_half) # Sol parçayı sırala (rekürsif)
        merge_sort(right_half) # Sağ parçayı sırala (rekürsif)

        merge(arr, left_half, right_half) # İki parçayı birleştir

def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i] # Küçük olan elemanı al
            i += 1
        else:
            arr[k] = right[j] # Küçük olan elemanı al
            j += 1
        k += 1

    while i < len(left): # Geriye kalan elemanları ekle
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right): # Geriye kalan elemanları ekle
        arr[k] = right[j]
        j += 1
        k += 1

def heapify(arr, n, i):
    largest = i # Başlangıçta en büyük değer indeksi i olarak belirlenir.
    left = 2 * i + 1 #Sol çocuk düğümün indeksi hesaplanır.
    right = 2 * i + 2 # Sağ çocuk düğümün indeksi hesaplanır.

    if left < n and arr[i] < arr[left]: #Sol çocuk düğümün dizi boyutunu aşmaması ve mevcut indeksteki değerden büyük olması kontrol edilir.
        largest = left

    if right < n and arr[largest] < arr[right]: #Sağ çocuk düğümün dizi boyutunu aşmaması ve en büyük olarak belirlenen değerden büyük olması kontrol edilir.
        largest = right
#En büyük değer mevcut indeksteki değerden farklıysa, swap yapılır ve bu değişiklik için heapify fonksiyonu tekrar çağrılır.
    if largest != i: #rekürsif çalışması sağlanır.
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr): #Bir max heap (veya min heap) oluşturur. Heap yapısını kullanarak en büyük elemanı çıkarır ve sıralı kısmı oluşturur.
#Her adımda, diziyi bir max heap olarak düşünüp en büyük elemanı kökten çıkarır.
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1): # ikiye böl bir dizinin yarısından bir önceki elemanın indeksini al, sondan başa doğru azaltarak git.
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def quick_sort(arr, low, high): #Bir pivot eleman seçer ve diziyi pivot etrafında iki alt diziye böler. Pivot eleman, doğru konumuna yerleştirilir.
#Her iki alt dizi için bu işlemi tekrar eder, rekürsif olarak sıralama yapar.
    if low < high:
        pi = partition(arr, low, high) ## Pivot indeksini belirle
        quick_sort(arr, low, pi - 1) #sol tarafı sıralamaca
        quick_sort(arr, pi + 1, high) #sağ tarafı sıralamaca

def partition(arr, low, high):
    pivot = arr[high] # Pivot elemanı olarak dizinin son elemanı
    i = low - 1  # Index'i belirleme
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Küçük elemanları sol tarafa yerleştir yine yer değiştirme işlemi
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Pivot elemanı ile işlem yapılan elemanı yer değiştir
    return i + 1 # Yeni pivot elemanın indeksini döndürme

# Ana program
arr_to_sort = [random.randint(1, 100) for _ in range(10)]
print("Orijinal dizi:", arr_to_sort)

choice = input("Hangi sıralama algoritmasını kullanmak istersiniz? (bubble/insertion/selection/merge/heap/quick): ")

start_time = time.time()  # Algoritma başlama zamanını kaydet
if choice == "bubble":
    bubble_sort(arr_to_sort)
elif choice == "insertion":
    insertion_sort(arr_to_sort)
elif choice == "selection":
    selection_sort(arr_to_sort)
elif choice == "merge":
    merge_sort(arr_to_sort)
elif choice == "heap":
    heap_sort(arr_to_sort)
elif choice == "quick":
    quick_sort(arr_to_sort, 0, len(arr_to_sort) - 1)
else:
    print("Geçersiz seçenek!")

end_time = time.time()  # Algoritma bitiş zamanını kaydet
elapsed_time = end_time - start_time  # Geçen süreyi hesapla


print("Sıralanmış dizi:", arr_to_sort)
print(f"{choice.capitalize()} sıralama algoritması {elapsed_time} saniyede çalıştı.")

arr_to_sort = [random.randint(1, 100) for _ in range(1000)]  # 1000 elemanlı rastgele bir dizi oluştur

# Bubble Sort'un çalışma süresini hesapla
start_time = time.time()
bubble_sort(arr_to_sort.copy())  # Bubble Sort'u kopyalanan dizi üzerinde çalıştır
end_time = time.time()
bubble_time = end_time - start_time

# Insertion Sort'un çalışma süresini hesapla
start_time = time.time()
insertion_sort(arr_to_sort.copy())  # Insertion Sort'u kopyalanan dizi üzerinde çalıştır
end_time = time.time()
insertion_time = end_time - start_time

# Selection Sort'un çalışma süresini hesapla
start_time = time.time()
selection_sort(arr_to_sort.copy())  # Selection Sort'u kopyalanan dizi üzerinde çalıştır
end_time = time.time()
selection_time = end_time - start_time

# Merge Sort'un çalışma süresini hesapla
start_time = time.time()
merge_sort(arr_to_sort.copy())  # Merge Sort'u kopyalanan dizi üzerinde çalıştır
end_time = time.time()
merge_time = end_time - start_time

# Heap Sort'un çalışma süresini hesapla
start_time = time.time()
heap_sort(arr_to_sort.copy())  # Heap Sort'u kopyalanan dizi üzerinde çalıştır
end_time = time.time()
heap_time = end_time - start_time

# Quick Sort'un çalışma süresini hesapla
start_time = time.time()
quick_sort(arr_to_sort.copy(), 0, len(arr_to_sort) - 1)  # Quick Sort'u kopyalanan dizi üzerinde çalıştır
end_time = time.time()
quick_time = end_time - start_time

# Süreleri ekrana yazdır
print("Bubble Sort süresi:", bubble_time)
print("Insertion Sort süresi:", insertion_time)
print("Selection Sort süresi:", selection_time)
print("Merge Sort süresi:", merge_time)
print("Heap Sort süresi:", heap_time)
print("Quick Sort süresi:", quick_time)



Bir pivot eleman seçer ve diziyi pivot etrafında iki alt diziye böler.
Pivot eleman, doğru konumuna yerleştirilir.
Her iki alt dizi için bu işlemi tekrar eder, rekürsif olarak sıralama yapar.
Zaman karmaşıklığı: O(n^2) (en kötü durumda), O(n log n) (ortalama durumda).
"""
