from extract import extract
from transform import transform
from load import load

print("=" * 40)
print("   🎬 MOVIE ETL PIPELINE STARTING")
print("=" * 40 + "\n")

extract()
print()
transform()
print()
load()

print("\n" + "=" * 40)
print("   ✅ PIPELINE COMPLETE!")
print("=" * 40)
