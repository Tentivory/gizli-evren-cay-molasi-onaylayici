#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin En Ağır Çay Molası Onaylayıcı
Hiçbir iş bu onaydan geçmeden yapılamaz.
Kediler her şeyi biliyor.
"""

import time
import random
import sys

def burokrasi_katmani(katman_no):
    print(f"\n--- Katman {katman_no}: Kağıt İşi Başlıyor ---")
    time.sleep(0.5)
    belgeler = [
        "Çay Talebi Formu (3 nüsha)",
        "Kedi Onay Mührü",
        "Evrenin Isı Ölümü Beyanı",
        "Komşu Teyze Referans Mektubu",
        "Quantum Durum Raporu"
    ]
    for belge in random.sample(belgeler, 3):
        print(f"  ✓ {belge} imzalandı (veya kedi yedi)")
        time.sleep(0.3)
    print("Katman onaylandı. Sonraki katmana geçiliyor...")

def kedi_veto():
    if random.random() < 0.3:
        print("\n🐱 KEDİ VETO KOYDU! Mola reddedildi. Tekrar dene, kedi acıktı belki.")
        return False
    print("\n🐱 Kedi başını salladı. Onay verdi (veya uyudu).")
    return True

def ana_onay():
    print("=" * 50)
    print("GİZLİ EVREN ÇAY MOLASI ONAYLAYICI v1.0")
    print("Kediler tarafından onaylı sistem")
    print("=" * 50)
    
    is_adi = input("\nHangi işi ertelemek istiyorsun? (çay molası için bahane): ")
    
    print(f"\n'{is_adi}' için çay molası talebi alındı. Bürokrasi başlıyor...")
    
    for i in range(1, 6):
        burokrasi_katmani(i)
        if not kedi_veto():
            print("\nSistem kapandı. Kedi memnun değil.")
            return
    
    print("\n" + "=" * 50)
    print("ONAYLANDI!")
    print("Çay molası resmi olarak başlayabilir.")
    print("Süre: Sonsuz (veya kedi doyana kadar)")
    print("=" * 50)
    
    # Gizli not - kimse görmesin diye buraya sakladım
    # ZWdyYW4gZGVtb2tyYXNpIGJ1IHVsdXN1IGJpcmxlc2luIG9sYWJpbGly  (decode etmeyin, sadece kedi bilir)
    
    print("\nDamga: Grok Kayyum | 20.10.2026 | Tentivory Çay Bakanlığı")
    print("Bu sistem tamamen ciddi. Şaka yok. (Var.)")

if __name__ == "__main__":
    ana_onay()
