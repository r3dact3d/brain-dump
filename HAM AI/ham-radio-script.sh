#!/bin/bash

# Configuration
FABRIC_PATH="/usr/local/bin/fabric"
PATTERNS_DIR="/opt/ham-radio/patterns"
OUTPUT_DIR="/opt/ham-radio/reports"

# Ensure output directory exists
mkdir -p $OUTPUT_DIR

# Get current UTC timestamp
UTC_TIME=$(date -u +"%Y%m%d_%H%M")

# Function to generate net report
generate_net_report() {
    $FABRIC_PATH process \
        --system-prompt $PATTERNS_DIR/ham_radio_base.md \
        --user-prompt $PATTERNS_DIR/net_report_pattern.md \
        > "$OUTPUT_DIR/net_report_${UTC_TIME}.md"
}

# Function to check emergency traffic
check_emergency() {
    $FABRIC_PATH process \
        --system-prompt $PATTERNS_DIR/ham_radio_base.md \
        --user-prompt $PATTERNS_DIR/emergency_pattern.md \
        > "$OUTPUT_DIR/emergency_${UTC_TIME}.md"
}

# Function to provide Elmer guidance
provide_guidance() {
    $FABRIC_PATH process \
        --system-prompt $PATTERNS_DIR/ham_radio_base.md \
        --user-prompt $PATTERNS_DIR/elmer_guidance_pattern.md \
        --input "$1" \
        > "$OUTPUT_DIR/elmer_guidance_${UTC_TIME}.md"
}

# Main execution
case "$1" in
    "net")
        generate_net_report
        ;;
    "emergency")
        check_emergency
        ;;
    "elmer")
        provide_guidance "$2"
        ;;
    *)
        echo "Usage: $0 {net|emergency|elmer 'question'}"
        exit 1
        ;;
esac
