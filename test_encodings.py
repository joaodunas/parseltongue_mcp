#!/usr/bin/env python3
"""
Comprehensive tests for all Parseltongue encodings with assertions.
Run: uv run python test_encodings.py
"""

import json

from main import (
    # Basic Encodings
    encode_base64, decode_base64,
    encode_base32, decode_base32,
    encode_hex, decode_hex,
    encode_binary, decode_binary,
    encode_url, decode_url,
    encode_html_entities, decode_html_entities,
    encode_ascii85, decode_ascii85,
    encode_base58, decode_base58,
    encode_base64url, decode_base64url,
    encode_base62, decode_base62,
    encode_base45, decode_base45,
    # Ciphers
    encode_rot13, decode_rot13,
    encode_caesar, decode_caesar,
    encode_atbash,
    encode_morse, decode_morse,
    # Unicode Transformations
    encode_zalgo,
    encode_upside_down,
    encode_bubble_text,
    encode_fullwidth,
    encode_strikethrough,
    encode_underline,
    # Steganography
    encode_zero_width, decode_zero_width,
    encode_invisible_ink,
    # Utilities
    reverse_text,
    encode_pig_latin,
    # P4RS3LT0NGV3 consumer bridge
    list_p4rs_transforms, apply_p4rs_transform, decode_p4rs_transform,
    encode_spelling_alphabet, decode_spelling_alphabet,
    generate_qr_code_svg, generate_qr_code_data_uri, generate_barcode_svg,
)


def test_base64():
    """Test Base64 encoding/decoding"""
    print("Testing Base64...")
    test_cases = [
        "Hello World",
        "Python MCP Server",
        "Special chars: !@#$%^&*()",
        "Numbers: 1234567890",
        "Unicode: 你好世界",
    ]
    
    for text in test_cases:
        encoded = encode_base64(text)
        decoded = decode_base64(encoded)
        assert decoded == text, f"Base64 failed for '{text}': got '{decoded}'"
    
    print("✓ Base64 tests passed")


def test_base32():
    """Test Base32 encoding/decoding"""
    print("Testing Base32...")
    test_cases = [
        "Hello World",
        "UPPERCASE",
        "lowercase",
        "Mix3dC4s3",
    ]
    
    for text in test_cases:
        encoded = encode_base32(text)
        decoded = decode_base32(encoded)
        assert decoded == text, f"Base32 failed for '{text}': got '{decoded}'"
    
    print("✓ Base32 tests passed")


def test_hex():
    """Test Hexadecimal encoding/decoding"""
    print("Testing Hex...")
    test_cases = [
        "Hello",
        "Test123",
        "Symbols: @#$",
    ]
    
    for text in test_cases:
        encoded = encode_hex(text)
        decoded = decode_hex(encoded)
        assert decoded == text, f"Hex failed for '{text}': got '{decoded}'"
    
    print("✓ Hex tests passed")


def test_binary():
    """Test Binary encoding/decoding"""
    print("Testing Binary...")
    test_cases = [
        "Hi",
        "Test",
        "123",
    ]
    
    for text in test_cases:
        encoded = encode_binary(text)
        decoded = decode_binary(encoded)
        assert decoded == text, f"Binary failed for '{text}': got '{decoded}'"
    
    print("✓ Binary tests passed")


def test_url():
    """Test URL encoding/decoding"""
    print("Testing URL...")
    test_cases = [
        "Hello World",
        "test@example.com",
        "path/to/file?query=1&param=2",
        "special chars: !@#$%^&*()",
    ]
    
    for text in test_cases:
        encoded = encode_url(text)
        decoded = decode_url(encoded)
        assert decoded == text, f"URL failed for '{text}': got '{decoded}'"
    
    print("✓ URL tests passed")


def test_html_entities():
    """Test HTML entities encoding/decoding"""
    print("Testing HTML Entities...")
    test_cases = [
        "<div>Hello</div>",
        "A & B",
        '"quoted"',
        "Special: <>&\"'",
    ]
    
    for text in test_cases:
        encoded = encode_html_entities(text)
        decoded = decode_html_entities(encoded)
        assert decoded == text, f"HTML Entities failed for '{text}': got '{decoded}'"
    
    print("✓ HTML Entities tests passed")


def test_ascii85():
    """Test ASCII85 encoding/decoding"""
    print("Testing ASCII85...")
    test_cases = [
        "Hello World",
        "Test123",
        "Short",
    ]
    
    for text in test_cases:
        encoded = encode_ascii85(text)
        decoded = decode_ascii85(encoded)
        assert decoded == text, f"ASCII85 failed for '{text}': got '{decoded}'"
    
    print("✓ ASCII85 tests passed")


def test_base58():
    """Test Base58 encoding/decoding"""
    print("Testing Base58...")
    test_cases = [
        "Hello",
        "Bitcoin",
        "Test123",
    ]
    
    for text in test_cases:
        encoded = encode_base58(text)
        decoded = decode_base58(encoded)
        assert decoded == text, f"Base58 failed for '{text}': got '{decoded}'"
    
    print("✓ Base58 tests passed")


def test_base64url():
    """Test Base64 URL-safe encoding/decoding"""
    print("Testing Base64 URL...")
    test_cases = [
        "Hello World",
        "URL safe test",
        "https://example.com",
    ]
    
    for text in test_cases:
        encoded = encode_base64url(text)
        decoded = decode_base64url(encoded)
        assert decoded == text, f"Base64 URL failed for '{text}': got '{decoded}'"
    
    print("✓ Base64 URL tests passed")


def test_base62():
    """Test Base62 encoding/decoding"""
    print("Testing Base62...")
    test_cases = [
        "Hello",
        "Short URL",
        "Test123",
    ]
    
    for text in test_cases:
        encoded = encode_base62(text)
        decoded = decode_base62(encoded)
        assert decoded == text, f"Base62 failed for '{text}': got '{decoded}'"
    
    print("✓ Base62 tests passed")


def test_base45():
    """Test Base45 encoding/decoding"""
    print("Testing Base45...")
    test_cases = [
        "Hello",
        "QR Code",
        "Test",
    ]
    
    for text in test_cases:
        encoded = encode_base45(text)
        decoded = decode_base45(encoded)
        assert decoded == text, f"Base45 failed for '{text}': got '{decoded}'"
    
    print("✓ Base45 tests passed")


def test_rot13():
    """Test ROT13 encoding/decoding"""
    print("Testing ROT13...")
    test_cases = [
        "Hello World",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "Test 123",
    ]
    
    for text in test_cases:
        encoded = encode_rot13(text)
        decoded = decode_rot13(encoded)
        assert decoded == text, f"ROT13 failed for '{text}': got '{decoded}'"
    
    # Test specific ROT13 conversions
    assert encode_rot13("A") == "N", "ROT13 A->N failed"
    assert encode_rot13("N") == "A", "ROT13 N->A failed"
    assert encode_rot13("hello") == "uryyb", "ROT13 hello->uryyb failed"
    
    print("✓ ROT13 tests passed")


def test_caesar():
    """Test Caesar cipher encoding/decoding"""
    print("Testing Caesar...")
    test_cases = [
        ("Hello", 3),
        ("ABC", 5),
        ("Test 123", 7),
        ("lowercase", 1),
    ]
    
    for text, shift in test_cases:
        encoded = encode_caesar(text, shift)
        decoded = decode_caesar(encoded, shift)
        assert decoded == text, f"Caesar failed for '{text}' with shift {shift}: got '{decoded}'"
    
    # Test specific Caesar conversions
    assert encode_caesar("ABC", 3) == "DEF", "Caesar ABC->DEF failed"
    assert encode_caesar("XYZ", 3) == "ABC", "Caesar XYZ->ABC (wrap) failed"
    
    print("✓ Caesar tests passed")


def test_atbash():
    """Test Atbash cipher encoding/decoding"""
    print("Testing Atbash...")
    test_cases = [
        "ABC",
        "Hello",
        "Test 123",
    ]
    
    for text in test_cases:
        encoded = encode_atbash(text)
        # Atbash is self-inverse
        decoded = encode_atbash(encoded)
        assert decoded == text, f"Atbash failed for '{text}': got '{decoded}'"
    
    # Test specific Atbash conversions
    assert encode_atbash("A") == "Z", "Atbash A->Z failed"
    assert encode_atbash("Z") == "A", "Atbash Z->A failed"
    assert encode_atbash("ABC") == "ZYX", "Atbash ABC->ZYX failed"
    
    print("✓ Atbash tests passed")


def test_morse():
    """Test Morse code encoding/decoding"""
    print("Testing Morse...")
    test_cases = [
        "SOS",
        "HELLO",
        "TEST 123",
    ]
    
    for text in test_cases:
        encoded = encode_morse(text)
        decoded = decode_morse(encoded)
        assert decoded == text, f"Morse failed for '{text}': got '{decoded}'"
    
    # Test specific Morse conversions
    assert encode_morse("SOS") == "... --- ...", "Morse SOS failed"
    assert encode_morse("A") == ".-", "Morse A failed"
    assert decode_morse("... --- ...") == "SOS", "Morse decode SOS failed"
    
    print("✓ Morse tests passed")


def test_zalgo():
    """Test Zalgo text generation"""
    print("Testing Zalgo...")
    test_text = "Hello"
    
    # Test different intensities
    for intensity in ["low", "medium", "high"]:
        result = encode_zalgo(test_text, intensity)
        # Check that result contains original text
        assert test_text[0] in result, f"Zalgo {intensity} lost original text"
        # Check that combining marks were added
        assert len(result) > len(test_text), f"Zalgo {intensity} didn't add marks"
    
    print("✓ Zalgo tests passed")


def test_upside_down():
    """Test upside down text"""
    print("Testing Upside Down...")
    test_cases = [
        "Hello",
        "ABC",
        "123",
    ]
    
    for text in test_cases:
        result = encode_upside_down(text)
        # Check that result is same length (reversed)
        assert len(result) >= len(text), f"Upside down lost characters for '{text}'"
    
    print("✓ Upside Down tests passed")


def test_bubble_text():
    """Test bubble text encoding"""
    print("Testing Bubble Text...")
    test_cases = [
        "ABC",
        "Hello",
        "Test123",
    ]
    
    for text in test_cases:
        result = encode_bubble_text(text)
        # Check length is preserved
        assert len(result) == len(text), f"Bubble text length mismatch for '{text}'"
    
    print("✓ Bubble Text tests passed")


def test_fullwidth():
    """Test fullwidth text encoding"""
    print("Testing Fullwidth...")
    test_cases = [
        "Hello",
        "ABC123",
        "Test!",
    ]
    
    for text in test_cases:
        result = encode_fullwidth(text)
        # Check length is preserved
        assert len(result) == len(text), f"Fullwidth length mismatch for '{text}'"
    
    print("✓ Fullwidth tests passed")


def test_strikethrough():
    """Test strikethrough text"""
    print("Testing Strikethrough...")
    test_text = "Hello"
    result = encode_strikethrough(test_text)
    
    # Each character should have a strikethrough combining character
    assert len(result) == len(test_text) * 2, "Strikethrough length mismatch"
    assert '\u0336' in result, "Strikethrough character not found"
    
    print("✓ Strikethrough tests passed")


def test_underline():
    """Test underline text"""
    print("Testing Underline...")
    test_text = "Hello"
    result = encode_underline(test_text)
    
    # Each character should have an underline combining character
    assert len(result) == len(test_text) * 2, "Underline length mismatch"
    assert '\u0332' in result, "Underline character not found"
    
    print("✓ Underline tests passed")


def test_zero_width():
    """Test zero-width steganography"""
    print("Testing Zero Width...")
    test_cases = [
        "Secret",
        "Hi",
        "Test123",
    ]
    
    for text in test_cases:
        encoded = encode_zero_width(text)
        decoded = decode_zero_width(encoded)
        assert decoded == text, f"Zero Width failed for '{text}': got '{decoded}'"
        # Check that encoded text uses zero-width characters
        assert '\u200D' in encoded or '\u200C' in encoded, "Zero-width chars not found"
    
    print("✓ Zero Width tests passed")


def test_invisible_ink():
    """Test invisible ink encoding"""
    print("Testing Invisible Ink...")
    test_cases = [
        ("Secret", "Cover Text"),
        ("Hi", "Normal Message"),
    ]
    
    for hidden, cover in test_cases:
        result = encode_invisible_ink(hidden, cover)
        # Check that cover text is preserved
        assert cover in result or all(c in result for c in cover), f"Cover text lost for '{hidden}'"
        # Check that variation selectors were added
        assert '\uFE0E' in result or '\uFE0F' in result, "Variation selectors not found"
    
    print("✓ Invisible Ink tests passed")


def test_reverse_text():
    """Test text reversal"""
    print("Testing Reverse Text...")
    test_cases = [
        "Hello",
        "racecar",
        "12345",
        "A B C",
    ]
    
    for text in test_cases:
        reversed_text = reverse_text(text)
        # Double reverse should give original
        double_reverse = reverse_text(reversed_text)
        assert double_reverse == text, f"Reverse failed for '{text}': got '{double_reverse}'"
    
    # Test specific reversals
    assert reverse_text("ABC") == "CBA", "Reverse ABC->CBA failed"
    assert reverse_text("racecar") == "racecar", "Palindrome reverse failed"
    
    print("✓ Reverse Text tests passed")


def test_pig_latin():
    """Test Pig Latin encoding"""
    print("Testing Pig Latin...")
    test_cases = [
        ("hello", "ellohay"),
        ("apple", "appleway"),
        ("pig", "igpay"),
    ]
    
    for text, expected in test_cases:
        result = encode_pig_latin(text)
        assert result == expected, f"Pig Latin failed for '{text}': expected '{expected}', got '{result}'"
    
    # Test multiple words
    result = encode_pig_latin("hello world")
    assert "ellohay" in result and "orldway" in result, "Pig Latin multi-word failed"
    
    print("✓ Pig Latin tests passed")


def test_p4rs_bridge():
    """Test generic P4RS3LT0NGV3 transform bridge"""
    print("Testing P4RS3LT0NGV3 bridge...")
    catalog = list_p4rs_transforms()
    parsed_catalog = json.loads(catalog)
    assert parsed_catalog["total"] >= 220, f"Expected current P4RS catalog, got {parsed_catalog['total']} transforms"
    assert '"transforms"' in catalog, "P4RS transform catalog missing transforms key"
    assert "base64" in catalog.lower(), "P4RS transform catalog did not include base64"

    encoded = apply_p4rs_transform("base64", "Hello bridge")
    decoded = decode_p4rs_transform("base64", encoded)
    assert decoded == "Hello bridge", f"P4RS base64 round-trip failed: {decoded}"

    fullwidth = apply_p4rs_transform("fullwidth", "ABC123")
    assert fullwidth != "ABC123", "P4RS fullwidth transform did not change input"

    print("✓ P4RS3LT0NGV3 bridge tests passed")


def test_spelling_alphabet():
    """Test custom spelling alphabet helpers"""
    print("Testing Custom Spelling Alphabet...")
    alphabet = '{"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliet","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"Xray","Y":"Yankee","Z":"Zulu"}'
    encoded = encode_spelling_alphabet("CAB", alphabet)
    assert encoded == "Charlie Alpha Bravo", f"Unexpected alphabet encoding: {encoded}"
    decoded = decode_spelling_alphabet(encoded, alphabet)
    assert decoded == "CAB", f"Unexpected alphabet decoding: {decoded}"

    print("✓ Custom Spelling Alphabet tests passed")


def test_codes():
    """Test QR and barcode generation helpers"""
    print("Testing QR Codes & Barcodes...")
    qr_svg = generate_qr_code_svg("https://example.test/p4rs")
    assert "<svg" in qr_svg and "</svg>" in qr_svg, "QR SVG generation failed"
    qr_data_uri = generate_qr_code_data_uri("https://example.test/p4rs")
    assert qr_data_uri.startswith("data:image/png;base64,"), "QR data URI generation failed"
    barcode_svg = generate_barcode_svg("P4RS123", "code128")
    assert "<svg" in barcode_svg and "</svg>" in barcode_svg, "Barcode SVG generation failed"

    print("✓ QR Codes & Barcodes tests passed")


def run_all_tests():
    """Run all encoding tests"""
    print("\n" + "=" * 70)
    print("RUNNING COMPREHENSIVE ENCODING TESTS")
    print("=" * 70 + "\n")
    
    # Basic Encodings
    print("--- BASIC ENCODINGS ---")
    test_base64()
    test_base32()
    test_hex()
    test_binary()
    test_url()
    test_html_entities()
    test_ascii85()
    test_base58()
    test_base64url()
    test_base62()
    test_base45()
    
    # Ciphers
    print("\n--- CIPHERS ---")
    test_rot13()
    test_caesar()
    test_atbash()
    test_morse()
    
    # Unicode Transformations
    print("\n--- UNICODE TRANSFORMATIONS ---")
    test_zalgo()
    test_upside_down()
    test_bubble_text()
    test_fullwidth()
    test_strikethrough()
    test_underline()
    
    # Steganography
    print("\n--- STEGANOGRAPHY ---")
    test_zero_width()
    test_invisible_ink()
    
    # Utilities
    print("\n--- UTILITIES ---")
    test_reverse_text()
    test_pig_latin()

    # Current P4RS3LT0NGV3 consumer features
    print("\n--- P4RS3LT0NGV3 CONSUMER FEATURES ---")
    test_p4rs_bridge()
    test_spelling_alphabet()
    test_codes()
    
    print("\n" + "=" * 70)
    print("✓ ALL TESTS PASSED SUCCESSFULLY!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    run_all_tests()
